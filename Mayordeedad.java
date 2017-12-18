
import java.io.*;

public class Mayordeedad {
	
	public static void main (String args[]) throws IOException{
		System.out.println("Introduzca su nombre");
		String Nombre;
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		Nombre = reader.readLine();
		System.out.println("Introduzca su edad");
		int Edad = Integer.parseInt(Edad);
		Edad = reader.readLine(Edad);
		if (Edad>=18) {
			System.out.println("Enorabuena, ya puedes ir a la carcel");
	} 
}

