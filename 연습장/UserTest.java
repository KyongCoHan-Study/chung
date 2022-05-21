import java.io.IOException;

public class UserTest {
	static class IllegalParamException extends RuntimeException {
		public IllegalParamException(String msg) {
			super(msg);
		}
	}
	
	static class Person {
		private String name;
		private int age;

		public Person(String name, int age) throws IOException {
			if (age < 0)
				throw new IllegalParamException("Invalid input age : " + age);
		}

		public String getName() {
			return name;
		}

		public int getAge() {
			return age;
		}
	}


	public static void main(String[] argv) {
		new UserTest().test();
	}

	private void test() {
		try {
			Person person = new Person("John", -10);
		} catch (IOException e) {
			System.out.println("Exception catched");
		} finally {
			System.out.println("execute finally block");
		}
	}


}