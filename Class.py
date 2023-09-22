class SubfieldsInA():
    def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
            print(temp)
class OddEven():
    def OddEven():
        num=int(input("Enter a Number:"))
        if(num%2==0):
            print("Even Number")
            cate="Even Number"
        else:
            print("Odd Number")
            cate="Odd Number"  
            return cate
class ElegiblityForMarriage():
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your age:"))
        if(gender in ("male")):
            if(age>21):
                print("ELIGIBLE")
                status="ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                status="NOT ELIGIBLE"
        elif(gender in ("female")):
                if(age>18):
                    print("ELIGIBLE")
                    status="ELIGIBLE"
                else:
                    print("NOT ELIGIBLE")
                    status="NOT ELIGIBLE"
                    return status
class FindPercent():
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5;
        print("Total",Total)
        per=float(Total*100/500);
        print("Percentage:","{:.12f}".format(per,2))
        return per
class triangle():
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter=height1+height2+breadth
        tri=(area,perimeter)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)
        return tri