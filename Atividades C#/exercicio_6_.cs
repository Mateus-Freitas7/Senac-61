
string[] valores = Console.ReadLine().Split(' ');

// Console.WriteLine("Digite o valor de A:");
// Console.WriteLine("Digite o valor de B:");
// Console.WriteLine("Digite o valor de C:");

double a = double.Parse(valores[0]);
double b = double.Parse(valores[1]);
double c = double.Parse(valores[2]);

double area_pi = 3.14159;


double triangulo = (a * c) /2;

double circulo = area_pi * (c*c);

double trapezio = (a+b) * c /2;

double area_pi = 3.14159;

double quadrado = b*b;

double retangulo = a*b;
 

 Console.WriteLine($"TRIÂNGULO:{triangulo}");
 Console.WriteLine($"CIRCULO:{circulo}");
 Console.WriteLine($"TRAPÉZIO:{trapezio}");
 Console.WriteLine($"QUADRADO:{quadrado}");
 Console.WriteLine($"RETÂNGULO:{retangulo}");






