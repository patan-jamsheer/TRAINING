def check_for_line():
    with open("practice.txt","r") as f1:
        word="python"
        line_no=1
        lines=True
        while lines:
            line=f1.readline()
            if(word in line):
                print(line_no)
                return
            line_no+=1
        return -1

def count_even_no():
    with open("practice.txt","r") as f:
        data=f.read()
        count=0
        list=data.split(",")
        for val in list:
            if int(val)%2==0:
                count+=1
        return count    

print(count_even_no())
