## Reproducibility 


1. Download Ollama from [ollama.com](https://ollama.com/) or install it via terminal:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. Start the Local LLM
Open your terminal and run the following command. It will automatically download the Qwen model and start the local API server. Leave this terminal window open in the background while you run the experiments.
code
```Bash
ollama run qwen2.5:7b
```

3. Install Python Dependencies
Open a new terminal window, navigate to this project repository, and install the required HTTP library:

```Bash
pip install requests
```

4. Run the Experiments
Execute the main orchestrator script to begin the tournament:

```Bash
python main.py
```
(might take 1 hour)

5. View the Results
Once the script finishes, it will automatically generate a results.txt file.
