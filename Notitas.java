/*
 * Eliminar nota
 */
import java.io.*;

public class  Notitas {
	
	public static void main (String args[]) throws IOException{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int i;
		int notas[];
		notas=new int[50];
		int Numnotas;
		System.out.println("Cuantos alumnos hay en clase");
		String texto = reader.readLine();
		int NumAlum= Integer.parseInt(texto);
			for (i=0;i<NumAlum;i++){
				System.out.println("Alumno " + (i + 1) + " Nota final: ");
				texto = reader.readLine();
				notas[i] = Integer.parseInt(texto);
			}
		System.out.println("Introduze una nota que quieras buscar");
		texto = reader.readLine();
		int Notbusc = Integer.parseInt(texto);
		if (Notbusc != notas[i]){
			System.out.println("No hay ninguna nota con valor " + Notbusc);
			
		}
		
	}
}	
