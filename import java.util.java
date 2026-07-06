import java.util.Scanner;

public class ConversorTemperaturas {

    // --- MÓDULO DE FUNCIONES (En Java se llaman métodos) ---
    
    public static double celsiusAFahrenheit(double celsius) {
        // Fórmula: (C * 9/5) + 32
        return (celsius * 9 / 5) + 32;
    }

    public static double celsiusAKelvin(double celsius) {
        // Fórmula: C + 273.15
        return celsius + 273.15;
    }

    // --- PROGRAMA PRINCIPAL ---
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("🌡️ CONVERSOR DE TEMPERATURAS");
        System.out.print("Ingrese los grados Celsius: ");
        double tempC = scanner.nextDouble();
        
        // Limpiar el buffer (importante después de leer un número)
        scanner.nextLine(); 

        System.out.println("\n¿A qué desea convertir?");
        System.out.println("1. Fahrenheit");
        System.out.println("2. Kelvin");
        System.out.print("Opción: ");
        String opcion = scanner.nextLine();

        if (opcion.equals("1")) {
            // Invocamos la función y guardamos el retorno
            double resultado = celsiusAFahrenheit(tempC);
            System.out.println(tempC + "°C equivalen a " + resultado + "°F");
            
        } else if (opcion.equals("2")) {
            double resultado = celsiusAKelvin(tempC);
            System.out.println(tempC + "°C equivalen a " + resultado + "K");
            
        } else {
            System.out.println("Opción inválida.");
        }

        scanner.close();
    }
}