// Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
// 2, 3, 7 -> 7
// 44 5 78 -> 78
// 22 3 9 -> 22


int max = 0;

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