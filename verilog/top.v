module top (
    input            clk,
    output reg [9:0] image_part
);
    reg fit_reg;
    reg [7:0] cnt;
    reg [99:0] res;
    reg entered;
    wire [1599:0] image_wire;
    wire [1599:0] res_wire;
    integer i;

    initial begin
        fit_reg = 1;
        cnt = 8'h00;
        entered = 1'b0;
    end

    rom ro (
        .clk   ( clk        ),
        .a     ( cnt        ),
        .image ( image_wire )
    );

    hopfield hf (
        .clk   ( clk        ),
        .fit   ( fit_reg    ),
        .image ( image_wire ),
        .out   ( res_wire   )
    );

    always @(posedge clk) begin
        if (cnt == 7) begin
            cnt = cnt + 1'b1;
            fit_reg = 1'b0;
        end
        if (cnt == 8 && !entered) begin
            entered = 1'b1;
            for (i = 0; i < 100; i = i + 1)
                res[i] = ($signed(res_wire[16*(i+1)-1:16*i]) >= 0) ? 1 : 0;
            i = 0;
        end
        if (entered) begin
            image_part = res[i+9:i];
            i = (i < 90) ? i + 10 : i;
        end
    end

endmodule
