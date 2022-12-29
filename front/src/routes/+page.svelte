<script>
	import PythonDivision from '$lib/pythonDivision.svelte';
	import PythonWithDecimals from '$lib/pythonWithDecimals.svelte';
	import PythonDivisionWithDecimals from '$lib/pythonWithDecimals.svelte';
	import './styles.css';
</script>

<svelte:head>
	<title>Dividers Demos</title>
	<meta name="Demo" content="A demo for a backend division algorithm." />
</svelte:head>

<section>
	<h1>Dividers demo!</h1>

	<p>
		Hello there, this is my working demo on <a href="svelte.dev">Svelte</a>
		for a <a href="https://www.python.org/">python</a>
		<a href="https://flask.palletsprojects.com">flask</a> API
	</p>

	<h2>Python Algorithm</h2>

	<p>
		Dividers API has a demonstration of the native division operator in python. We divide two
		numbers a/b, resulting in a float.
	</p>

	<p>
		If the result is larger than zero, later it will be rounded down (with the math.floor function)
		to the nearest integer; if it's less than zero, then it will be rounded up (with the math.ceil
		function) to the nearest integer.
	</p>

	<p>To get the rest we simply subtract from the numerator the quotient.</p>

	<PythonDivision />

	<h2>Get all decimals!</h2>
	<p>
		Lately, I've wanted to study repeated decimals of prime numbers divisions. So I made a function
		that returns an array of each division step.
	</p>
	<p>
		To go a step further in the division, multiply by ten the rest and use it as the new numerator
		for the division (this is what some of us learned as 'long-division' in school).
	</p>
	<p>Try it and see!</p>

	<PythonWithDecimals/>
</section>

<style>
	section {
		width: 50%;
		margin: auto;
	}
</style>
