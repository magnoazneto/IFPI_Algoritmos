int maior_valor(int a, int b){
    if (a > b){
        return a;
    }
    else{
        return b;
    }
}


void split(string str, string separator, vector* results)
{
    int found;
    found = str.find_first_of(separator);

    while(found != string::npos)
    {
        if(found > 0)
        {
            results->push_back(str.substr(0,found));
        }
		
        str = str.substr(found+1);
        found = str.find_first_of(separator);
    }

    if(str.length() > 0)
    {
        results->push_back(str);
    }
}
