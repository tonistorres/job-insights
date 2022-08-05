MENU="
---------------------------------
Program Project Job Insights
---------------------------------
0 - Exit
1 - Check error lint flake8
2 - Execute function in file testing corresponding
3 - Activate Environment Virtual Python
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
read -p "Enter the option [0,1,2,3] -->> " OPTION

if [ "$OPTION" -eq 2 ];then
read -p "Enter name function testing ex: test_xablau:" NAME
python3 -m pytest -k $NAME
exit 1
fi
}

INPUT

case "$OPTION" in
        
        1)
        python3 -m flake8 
        ;;

        3)
        cd ..
        pwd
        sleep 2
        source .venv/bin/activate
        ;;

        *)
        OPTIONJOKER
        ;;
esac      

