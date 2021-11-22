import gpt_2_simple as gpt2
from datetime import datetime
import scraper

# "124M" is the smallest available model. "355M", "774M", and "1558M" are also available as options that will produce higher fidelity outputs at the expense of more compute.
gpt2.download_gpt2(model_name="124M")
with open("Training Input.txt", "r", encoding="UTF-8") as file:
    input = file.read()
sess = gpt2.start_tf_sess()
# All parameters used by .finetune() are flexible and the specific ones here are esentially placeholders.
# The model produced by this is automatically saved locally and can be reused to avoid repeatdly training it.
gpt2.finetune(sess,
              dataset=input,
              model_name='124M',
              steps=1000,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=200,
              save_every=500
              )
output = gpt2.generate(sess, run_name='run1')
with open("Training Output.txt", "w", encoding="UTF-8") as file:
    file.write(output)
