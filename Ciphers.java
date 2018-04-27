import java.util.HashMap;


public class Ciphers {

	
	public static String Caesar_encrypt(String str, int shift){
		
		
		String abc = "abcdefghijklmnopqrstuvwxyz";
		HashMap<Integer, Character> map = new HashMap<Integer, Character>();
		for(int i = 0; i < abc.length(); i++){
			map.put(i + 1, abc.charAt(i));
		}
		
		HashMap<Integer, Character> new_map = new HashMap<Integer, Character>();
		
		for(Integer key : map.keySet()){
			Character letter = map.get(key);
			if(key + shift > 26){
				int difference = (key + shift - 26);
				new_map.put(difference, letter);
			}
			else{
				new_map.put(key + shift, letter);
			}
		}
		
	
		//index - letter
		String ans = "";
		for(int i = 0; i < str.length(); i++){
			int initial_index = 0;
			for(int j = 0; j < abc.length(); j++){
				if(str.charAt(i) == abc.charAt(j))
					initial_index += j + 1;
			}
			
			int newIndex;
			if(initial_index + shift > 26)
				newIndex = (initial_index + shift) - 26;
			else
				newIndex = initial_index + shift;
			
			Character letter = map.get(newIndex);
			ans += letter;
			
		}
		
		
	
		return ans;
		
		
	}
	
	public static void main(String[] args){
		
		String s = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk";
		String x = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr";
				
		for(int i = 0; i < 24; i++){
		String str = Caesar_encrypt(x, i);
		System.out.println(str + "sss");
		}
	}
}
