class Print{
    public static void main(String[] a){
        for(int i = 0; i<10; i++){
            if(i%3==0 && i%5==0){
                System.out.println(i + " amalowa 3 ndi 5");
            }
            else if(i%5==0){
                System.out.println(i + " amalowa 5 yekha");
            }
            else if(i%3==0){
                System.out.println(i + " amalowa 3 yekha");
            }
            else{
                System.out.println("komanso zinthu zake");
            }
        }
    }
}