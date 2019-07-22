import java.util.*;
class Main {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int t = Integer.parseInt(s.nextLine());

        for(int k=0;k<t;k++){
            String str = s.nextLine();
            int mseq = 0;
            int start = 0, end = str.length()-1;
            while(start < end){
                if(str.charAt(start) == '(' && str.charAt(end) == ')'){
                    start = start + 1;
                    end = end - 1;
                    mseq++;
                }
                if(str.charAt(start) == ')')
                    start += 1;
                if (str.charAt(end) == '(')
                    end -= 1;
            }
            System.out.println(mseq*2);
        }
    }
}
