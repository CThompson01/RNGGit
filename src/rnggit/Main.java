package rnggit;

public class Main {
	
	static int[] myIntArray = new int[5];
	
	public static void main(String[] args) {
		for (int i = 0; i < myIntArray.length; i++) {
			if ((int)(Math.random() * 10) >= 5) {
				myIntArray[i] = 1;
			} else {
				myIntArray[i] = 0;
			}
		}
	}

}
