
function a = sim_test(input)
disp(input)
for i = 1:100000000
    if mod(i, 10000000) == 0
        disp(i)
    end
end
a = i;
end
