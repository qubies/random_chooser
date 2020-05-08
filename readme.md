#Random Victim Chooser
 
CLI utility that lets you build a list of strings and then sample the list either with or without replacement. 

## Setup
```
git clone https://github.com/qubies/random_chooser.git
cd random_chooser
```

## Run
if you want the changes made to choices.json to persist (keep the list for the future):
```
docker build -t "chooser" . && docker run --rm -tiv $(pwd):/code chooser 
```
else 
`docker build -t "chooser" .` 
then
`docker run --rm -ti chooser` 
