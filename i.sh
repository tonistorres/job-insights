MENU="
---------------------------------
Program Project Job Insights
---------------------------------
0 - Exit
1 - Check error lint flake8
"

OPTIONJOKER(){
    echo -e "\033[31m -------------------------------------- \033[m"
    echo -e "\033[31m Option $OPTION unknown \033[m"
    echo -e "\033[31m -------------------------------------- \033[m"
        echo -e "\033[31m [Exit 1s] \033[m"
        sleep 1
        exit 1     
   echo -e "\033[31m -------------------------------------- \033[m"
    
}

INPUT(){
echo "$MENU "
read -p "Enter the option [0,1] -->> " OPTION
}

INPUT

case "$OPTION" in
        
        1)
        python3 -m flake8 
        ;;
               
        *)
        OPTIONJOKER
        ;;
esac      

