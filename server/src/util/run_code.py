import os
import json
import traceback

def main():
    try:
        code = os.environ.get("CODE", "")
        
        global_outputs = {"output": ""}
        
        # Print function to capture print statements
        def custom_print(*args, **kwargs):
            global_outputs["output"] += " ".join(map(str, args)) + "\n"
        
        exec(code, {"print": custom_print}, global_outputs)

        result = {
            "success": True,
            "output": global_outputs["output"]
        }
    
    # Capturing exception details
    except Exception as e:
        result = {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }

    print(json.dumps(result))

if __name__ == "__main__":
    main()
