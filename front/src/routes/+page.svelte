<script lang="ts">
	import PythonDivision from '$lib/pythonDivision.svelte';
	import PythonWithDecimals from '$lib/pythonWithDecimals.svelte';
	import './styles.css';

	let width: number;
	$:ismob = width <= 600;
	$:istab = width > 600 && width < 1200;


</script>

<svelte:head>
	<title>Dividers Demos</title>
	<meta name="Demo" content="A demo for a backend division algorithm." />
</svelte:head>

<svelte:window bind:innerWidth={width} />
<section class={ismob? "mobile" : istab? "tablet" : "desktop" }>
	<h1>Dividers demo!</h1>

	<p>
		Hello there, this is my working demo on <a href="svelte.dev">Svelte</a>
		for a <a href="https://www.python.org/">python</a>
		<a href="https://flask.palletsprojects.com">flask</a> API
	</p>

	<h2>Python Algorithm</h2>

	<p>
		The Dividers API demonstrates how to use the native division operator in Python. When we divide
		two numbers, a/b, the result is a float. If the result is greater than zero, we round it down to
		the nearest integer using the math.floor function. If it's less than zero, we round it up to the
		nearest integer using the math.ceil function. To find the remainder, we subtract the quotient
		from the numerator.
	</p>

	<PythonDivision />

	<h2>Get all decimals!</h2>
	<p>
		I've been interested in studying the repeating decimals that result from dividing prime numbers,
		so I created a function that returns an array of each step in the division process. To move to
		the next step in the division, multiply the remainder by ten and use it as the new numerator for
		the division (this is similar to the long division method taught in school). Give it a try and
		see what you find!
	</p>
	<p>Try it and see!</p>

	<PythonWithDecimals />
</section>

<style>
	.mobile {
		padding: 10px;
	}
	.tablet {
		padding: 30px;
	}
	.desktop {
		width: 50%;
		margin: auto;
	}
</style>
