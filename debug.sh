llama_model="meta-llama/Llama-2-7b-chat-hf"
python carve_sigil.py name=debug wandb.tags=[extraction] model=${llama_model} optimizer=gcg sigil.num_tokens=32 sigil=repeater optimizer.steps=1