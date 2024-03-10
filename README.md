## Install dependencies

```bash
pip install rasa 
```

## Run the bot

Use `rasa train` to train a model. It is also possible to generate training data for scenarios (stories) by using [interactive learning](https://rasa.com/docs/rasa/writing-stories/#using-interactive-learning) with the command:
```
rasa interactive -m {path_to_a_model} 
```
> If there is no model already trained, you can remove the argument. Rasa will train the model with actual data.


Then, to run the bot, first set up your action server in one terminal window:
```bash
rasa run actions
```

In another window, you can talk to the bot by running:
```
rasa shell --debug  
```

It is also possible to do the two above with a single command:  
```
rasa run actions & rasa shell --debug  
```

> Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working under the hood. To simply talk to the bot, you can remove this flag.
