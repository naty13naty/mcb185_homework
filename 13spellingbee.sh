cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "r" | grep -E "^[aizncro]{4,}$" 
