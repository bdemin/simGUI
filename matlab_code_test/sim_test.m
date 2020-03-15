
function sim_test()

for i = 1:100000000
    if mod(i, 10000000) == 0
        disp(i)
    end
end

x = linspace(0, 4*pi);
y = sin(x);
plot(x,y)

end
