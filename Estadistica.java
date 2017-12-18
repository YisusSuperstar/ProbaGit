/*
 * Estadística de notas 
 */
import java.io.*;

public class  Estadistica {
	
	public static void main (String args[]) throws IOException{
		int i;
		int notas[];
		int Media;
		int Med;
		int NotBaj;
		int NotAlt;
		Media=0;
		NotBaj=11;
		NotAlt=0;
		notas=new int[10];
		System.out.println("Cuantos alumnos hay en clase");
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String texto = reader.readLine();
		int NumAlum= Integer.parseInt(texto);
		
		for (i=0;i<NumAlum;i++){
			System.out.println("Alumno " + (i + 1) + " Nota final: ");
			texto = reader.readLine();
			notas[i] = Integer.parseInt(texto);
			Media=Media+notas[i];
			if (NotBaj>notas[i]){
				NotBaj=notas[i];
			}
			if (NotAlt<notas[i]){
				NotAlt=notas[i];
			}	
				
		}
		Med=Media/i;
		System.out.println("La media de clase es " + Med);
		System.out.println("La nota más baja es " + NotBaj);
		System.out.println("La nota más alta es " + NotAlt);
		
	}
}	

