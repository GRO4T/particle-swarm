rm gifs/* logs/* graphs/*
for f in ./experiments/*/*.sh; do
  time bash "$f" 
done