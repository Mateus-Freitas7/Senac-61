class Retangulo()
{
    public double Lagura;
    public double Altura;

    public double Area()
    {
        return Lagura * Altura; // Resulta em 12
    }

    public double Perimetro()
    {
        return (Altura + Lagura) *2; // Resulta em 14 se as respectivas entradas forem 3 e 4 
    }

    public double Diagonal()
    {
        return Math.Sqrt((Lagura*Lagura) + (Altura*Altura));
        
    }
}



// Código do program cs

Retangulo valor;

valor = new Retangulo;
valor = new Retangulo;


Console.WriteLine("Entre com a altura e largura:");
string[] valores = Console.ReadLine().Split(" ");

valor.Largura = double.Parse(valores[0]);
valor.altura = double.Parse(valores[1]);



Console.WriteLine($"Àrea: {valor.Area()}");
Console.WriteLine($"Perímetro: {valor.Perimetro()}");
Console.WriteLine($"Diagonal: {valor.Diagonal()}");
