def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	if len(C) == 2:
		[[a, b], [c, d]] = C

		det = a * d - b * c

		inv_C = [
			[d / det, -b / det],
			[-c / det, a / det]
		]

	else:
		[[a, b, c], [d, e, f], [g, h, i]] = C

		det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

		inv_C = [
			[(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
			[(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
			[(d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det]
		]

	n = len(C)
	P = []
	for row_C in inv_C:
		new_row = []
		for col_idx in range(n):
			val = sum(row_C[k] * B[k][col_idx] for k in range(n))
			new_row.append(round(val, 4))
		P.append(new_row)

	return P