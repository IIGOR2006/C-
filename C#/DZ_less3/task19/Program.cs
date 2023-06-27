// See https://aka.ms/new-console-template for more information

Console.WriteLine("введите пятизначное число");
string num = Convert.ToInt32(Console.ReadLine());


void number(string num)
{
    if (num[0] == num[4] && num[1] == num[3])
    {
        Console.Write($"ваше число {num} - палидром");
    }

    else
    Console.WriteLine($"Ваше число: {num} - не палиндром");

}

if (num!.Length == 5)
{
    number(num);
}
else
Console.WriteLine($"введите правильное число");