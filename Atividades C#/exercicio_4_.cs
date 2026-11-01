
float salario;
Console.WriteLine("Digite seu número de funcionário:");
int number =  int.Parse (Console.ReadLine());

Console.WriteLine("Digite seu número de horas trabalhadas:");
int hours_worked =  int.Parse (Console.ReadLine());

Console.WriteLine("Digite o valor recebido por hora trabalhada:");
int  value =  int.Parse (Console.ReadLine());

salario = value * hours_worked;

Console.WriteLine($"Number: {number}");
Console.WriteLine($"Salário: {salario:F2}");
