public class UserTest {
	
	public static void main(String[] argv) {

		String stringObj = "Hello";
		int intValue = 0;
		Float floatObj = new Float(1.0);

		setValues(stringObj, intValue, floatObj);

		System.out.println( stringObj + ", "
				+ intValue + ", " + floatObj );

	}

	public static void setValues(String strValue, int intValue, Float floatObj) {
		strValue.replace("H", "h");
		strValue += " World";
		intValue = 99;
		floatObj.valueOf((float) 2.0);
	}
}