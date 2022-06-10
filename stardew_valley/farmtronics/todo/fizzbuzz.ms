for i in range(1, 100)
    output = ""

    if ((i % 3) == 0) then
        output = output + "Fizz"
    end if

    if ((i % 5) == 0) then
        output = output + "Buzz"
    end if

    if (output == "") then
        output = i
    end if

    print output
end for