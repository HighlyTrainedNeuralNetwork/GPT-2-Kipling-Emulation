# GPT-2-Kipling-Emulation
scraper.py pulls published Kipling poems from http://www.poetryloverspage.com/poets/kipling/kipling_ind.html and formats them such that they can be used as single input to train a text generation model on.

model.py uses the input produced by scraper and gpt-2-simple, https://github.com/minimaxir/gpt-2-simple, to quickly tune an existing GPT-2 model. This model can then be used to generate emulations of Kipling's work.
