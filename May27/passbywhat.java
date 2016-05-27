class PassByWhat {

	public static void main(String []args) {
		// Initialize new array
		int arr[] = {1};
		// Add two
		addTwo(arr);
		// Will print 3, explanation in the method.
		System.out.println(arr[0]);

		// Working with dude
		// Instantiate dude
		Dude dude = new Dude();
		// Give him a name
		dude.name = "Forkajduus";
		// Rename. Dude WILL be renamed.
		renameDude(dude);
		System.out.println(dude.name);
		// Change dude. Won't work.
		changeDude(dude);
		System.out.println(dude.name);
	}

	public static void addTwo(int []arr) {
		/* arr[0] will be 3. This happens because Java passes reference
		 * by value, thus arr is the value of the reference. arr points
		 * to the array, and this is a reason why arr[0] will be 3.
		 */
		arr[0] += 2;
	}

	public static void renameDude(Dude dude) {
		/* Dude will be successfully renamed to Jongional beause variable
		 * dude contains a value of the reference to the original dude.
		 */
		dude.name = "Jongional";
	}

	public static void changeDude(Dude dude) {
		/* dude variable contains a value of the reference. newDude is
		 * instantiated and itilialized with name "Hujakion". newDude
		 * assigned to the dude variable. Original dude won't be affected
		 * because dude variable now just holds a value to the newDude.
		 */
		Dude newDude = new Dude();
		newDude.name = "Hujakion";
		dude = newDude;
	}


	static class Dude {

		public String name;

	}

}