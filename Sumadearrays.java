/*
 * Suma de arrays
 */
import java.io.*;

public class Sumadearrays {
	
	public static void main (String args[]) throws IOException{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int i;
		int x;
		int y;
		int Num;
		int Num2;
		int Num3;
		int array[];
		int array2[];
		int array3[];
		array=new int[10];
		array2=new int[10];
		array3=new int[10];
		System.out.println("Introduzca un número");
		String texto = reader.readLine();
		Num= Integer.parseInt(texto);
		System.out.println("Introduzca otro número");
		String texto1 = reader.readLine();
		Num2= Integer.parseInt(texto1);
		Num3=Num+Num2;
		for (i=0;i<10;i++){
			array[i]=Num++;
			System.out.print(array[i] + ",");
		}
		System.out.println("");
		for (x=0;x<10;x++){
			array2[x]=Num2++;
			System.out.print(array[x] + ",");
		}
		System.out.println("");
		for (y=0;y<10;y++){
			array3[y]=Num3++;
			System.out.print(array[y] + ",");
		}
	}
}

