import google.generativeai as genai
import sys
import io
import traceback
import os
from dotenv import load_dotenv
load_dotenv(override=True)

class ADKBaseAgent:
    def __init__(self, name, role_prompt, model_name="gemini-2.5-flash"):
        self.name = name
        self.role_prompt = role_prompt
        
        # Pulls the API key from your environment securely
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set!")
            
        genai.configure(api_key=api_key)
        
        # Initialize the model with the system instruction (ADK standard)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=self.role_prompt
        )

    def execute_task(self, task_description, max_retries=3):
        """
        The ADK execution loop. The agent reasons, writes code, runs it, 
        and actively recovers if it encounters a Python error.
        """
        chat = self.model.start_chat(history=[])
        current_prompt = f"Task: {task_description}\nProvide ONLY executable Python code to solve this. No markdown blocks, no explanations. Just the raw code."
        
        for attempt in range(max_retries):
            print(f"\n[{self.name} - STATE: REASONING] (Attempt {attempt + 1}/{max_retries})")
            
            # 1. Agent Generates Code
            response = chat.send_message(current_prompt)
            code_to_run = response.text.replace("```python", "").replace("```", "").strip()
            
            print(f"[{self.name} - STATE: EXECUTING CODE]")
            
            # 2. Capture the output safely
            old_stdout = sys.stdout
            redirected_output = io.StringIO()
            sys.stdout = redirected_output
            
            success = False
            error_msg = ""
            
            try:
                # Executes the generated Python code
                exec(code_to_run, globals())
                success = True
            except Exception as e:
                error_msg = traceback.format_exc()
            finally:
                sys.stdout = old_stdout
                
            # 3. Agentic Recovery Logic
            if success:
                output = redirected_output.getvalue()
                print(f"[{self.name} - STATE: SUCCESS]\nOutput:\n{output}")
                return True, output
            else:
                print(f"[{self.name} - STATE: RECOVERY PROTOCOL INITIATED]")
                print(f"[{self.name} - ERROR DETECTED]:\n{error_msg}")
                # Feed the error back to the agent so it can fix its own code
                current_prompt = f"The previous code failed with this traceback:\n{error_msg}\nRewrite the code to fix this error. Return ONLY raw executable Python code."
                
        print(f"[{self.name} - STATE: FATAL ERROR] Task failed after {max_retries} attempts.")
        return False, "Task failed."