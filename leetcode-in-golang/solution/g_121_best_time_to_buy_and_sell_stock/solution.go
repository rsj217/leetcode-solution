package g_121_best_time_to_buy_and_sell_stock

func maxProfit(prices []int) int {
	ans := 0
	minPrice := prices[0]

	for _, curPrice := range prices {
		if curPrice < minPrice {
			minPrice = curPrice
		} else if ans < (curPrice - minPrice) {
			ans = curPrice - minPrice

		}
	}
	return ans
}
