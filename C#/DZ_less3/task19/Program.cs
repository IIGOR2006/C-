// See https://aka.ms/new-console-template for more information

console.WriteLine("введите пятизначное число");
int num = Convert.ToInt32(console.ReadLine());

string num = Convert.ToString(num);

void number(string num)
{
    if (num[0] == num[4] && num[1] == num[3])
    {
        console.Write($"ваше число {num} - палидром");
    }

    else
    console.WriteLine($"Ваше число: {num} - не палиндром");

}

if (num!.Length == 5)
{
    number(num);
}
else
console.WriteLine($"введите правильное число")