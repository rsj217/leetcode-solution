package g_121_best_time_to_buy_and_sell_stock

func maxProfit(prices []int) int {
	ans := 0
	prePrice := prices[0]
	for _, curPrice := range prices[0:] {
		if prePrice < curPrice {
			ans += curPrice - prePrice
		}
		prePrice = curPrice
	}
	return ans
}
