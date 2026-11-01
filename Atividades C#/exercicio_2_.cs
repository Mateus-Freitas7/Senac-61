
 using Math;
float pi = 3.14159f;
double area;

Console.WriteLine("Digite o valor do raio de um círculo:");
float raio  = float.Parse (Console.ReadLine());

area = pi * Math.Pow(raio, 2); // A var raio é a base e o 2 é o expoente


Console.WriteLine($"O valor do raio do círculo é de {area:F4}");

