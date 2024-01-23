echo Natnael Tsegai # Khalid Saif
echo $USER

cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "a" | grep -E "^[cfmouta]{3,}$"
gunzip -c dictionary.gz | grep -E "b" | grep -E "^[trnliab]{3,}$"
gunzip -c dictionary.gz | grep -E "c" | grep -E "^[amdinoac]{3,}$"
gunzip -c dictionary.gz | grep -E "z" | grep -E "^[naigroaz]{3,}$"

cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "a" | grep -E "^[cfmouta]{3,}$" | wc
gunzip -c dictionary.gz | grep -E "b" | grep -E "^[trnliab]{3,}$" | wc
gunzip -c dictionary.gz | grep -E "c" | grep -E "^[amdinoac]{3,}$" | wc
gunzip -c dictionary.gz | grep -E "z" | grep -E "^[naigroaz]{3,}$" | wc
