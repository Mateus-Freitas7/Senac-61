

// Console.WriteLine("Digite um número:");
// int numero = int.Parse(Console.ReadLine());


// if (numero < 0)
// {
//     Console.WriteLine($"O número{numero} é negativo");
// }
// else
// {
//     Console.WriteLine($"O número {numero} não é negativo");
// }



// Console.WriteLine("Digite um número:");
// int numero = int.Parse(Console.ReadLine());


// if (numero % 2 == 0)
// {
//     Console.WriteLine($"O número{numero} é PAR!");
// }
// else
// {
//     Console.WriteLine($"O número {numero} é ÍMPAR!");
// }


Console.WriteLine("Digite um número:");
int numero = int.Parse(Console.ReadLine());

Console.WriteLine("Digite um número:");
int numero_2 = int.Parse(Console.ReadLine());


if (numero % numero_2 == 0 || numero_2 % numero  == 0) 
{
    Console.WriteLine($"São multíplos!");
}
else
{
    Console.WriteLine($"Não são multíplos!");
}