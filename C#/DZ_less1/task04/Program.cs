// See https://aka.ms/new-console-template for more information

int max = 0;
int min = 0;

Console.Write("Введите первое число: ");
int Number1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите второе число: ");
int Number2 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите третье число: ");
int Number3 = Convert.ToInt32(Console.ReadLine());

if(Number1 > Number2 && Number1 > Number3)
{
    max = Number1;
}
else
{
    if(Number2 > Number3)
    {
        max = Number2;
    }
    else
    {
        max = Number3;
    }
}
Console.WriteLine("max = " + max);