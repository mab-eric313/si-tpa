export function formatRupiah(num) {
	return new Intl.NumberFormat("id-ID", {
		style: "currency",
		currency: "IDR"
	}).format(num);
}

export function formatRibuan(num) {
	if (!num) return "";
	return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

export function handleInput(e, inputBendahara) {
	const rawValue = e.target.value.replace(/[^0-9]/g, '');
	const parsedValue = rawValue ? parseInt(rawValue, 10) : 0;
	
	inputBendahara.nominal = parsedValue;
	e.target.value = formatRibuan(parsedValue);
}

