<template>
	<v-app>
		<v-app-bar app color="primary" dark>
			<v-toolbar-title class="heading">Apify Eshop Matcher</v-toolbar-title>
		</v-app-bar>

		<v-main>
			<v-select class="ma-10" :items="items" v-model="eshopname" label="Choose eshop view"></v-select>
			<v-container grid-list-xs class="eshops">
				<div class="mx-5 fullw">
					<h1 class="eshopname mb-2">
						{{ eshopname.toUpperCase() }}
					</h1>
					<v-card class="mx-auto">
						<v-list>
							<v-list-group v-for="product in eshop" :key="product.id" v-model="product.active" no-action>
								<template v-slot:activator>
									<v-list-item-content>
										<v-list-item-title>
											<v-row>
												<v-col cols="8" class="flexx">
													<h3>
														{{ product.name.toUpperCase() }}
														<price :price="product.price" />
														<v-btn fab small class="elevation-1" color="primary" @click.stop target="_blank" :href="product.url">
															<v-icon small>
																mdi-cart-arrow-right
															</v-icon>
														</v-btn>
													</h3>
												</v-col>
												<v-col cols="4" class="d-flex justify-end">
													<v-chip class="ma-2 goright" color="grey" v-if="product.duplicates.length">
														{{ product.duplicates.length }}
													</v-chip>
													<v-chip class="ma-2 white--text" color="red" v-if="Object.keys(product.similar_listings).length">
														{{ Object.keys(product.similar_listings).length }}
													</v-chip>
												</v-col>
											</v-row>
										</v-list-item-title>
									</v-list-item-content>
								</template>

								<template v-if="product.duplicates.length">
									<span class="ml-10 subtitle-1">Same products in {{ eshopname }}</span>
									<v-list-item v-for="duplicatID in product.duplicates" :key="duplicatID" class="mt-2">
										<v-list-item-content>
											<v-list-item-title>
												{{ findByIdInEshop(duplicatID, data[eshopname]).name }}
												<price :price="findByIdInEshop(duplicatID, data[eshopname]).price" />
												<v-btn fab small class="elevation-1" color="primary" @click.stop target="_blank" :href="product.url">
													<v-icon small>
														mdi-cart-arrow-right
													</v-icon>
												</v-btn>
											</v-list-item-title>
										</v-list-item-content>
									</v-list-item>
								</template>

								<span class="ml-10 subtitle-1">Same products by competitions</span>
								<v-list-item v-for="(item, key) in product.similar_listings" :key="key" class="mt-1">
									<v-list-item-content>
										<!-- <v-divider class="mt-4"></v-divider> -->
										<v-list-item-title>
											<span class="title mr-3">{{ key.toUpperCase() }}:</span> {{ findByIdInEshop(product.similar_listings[key], data[key]).name.toUpperCase() }}
											<price :price="findByIdInEshop(product.similar_listings[key], data[key]).price" />
											<v-btn fab small class="elevation-1" color="primary" @click.stop target="_blank" :href="product.url">
												<v-icon small>
													mdi-cart-arrow-right
												</v-icon>
											</v-btn>
											<!-- <v-divider class="mt-4"></v-divider> -->
										</v-list-item-title>
									</v-list-item-content>
								</v-list-item>
							</v-list-group>
						</v-list>
					</v-card>
				</div>
			</v-container>
		</v-main>
	</v-app>
</template>

<script>
// import alzaData from "@/dataLoader";
import Products from "@/components/Products.vue";
// import SimiliarListing from "./components/SimiliarListing";
import price from "@/components/Price";

export default {
	name: "App",

	data() {
		return {
			items: ["alza", "czc", "mironet", "mall"],
			eshopname: "alza",
		};
	},

	created() {
		this.alzaData = require("../.././alza.json");
		this.czcData = require("../.././czc.json");
		this.mallData = require("../.././mall.json");
		this.mironetData = require("../.././mironet.json");
		// this.data = this.alzaData;
		// console.log("data", this.alzaData);
	},

	computed: {
		data() {
			if (this.eshopname == "alza") {
				return this.alzaData;
			} else if (this.eshopname == "czc") {
				return this.czcData;
			} else if (this.eshopname == "mall") {
				return this.mallData;
			} else if (this.eshopname == "mironet") {
				return this.mironetData;
			}
		},

		eshop() {
			return this.data[this.eshopname];
		},
	},

	components: {
		// SimiliarListing,
		price,
	},

	methods: {
		findByIdInEshop(id_tosearch, eshop) {
			// console.log("eshop", eshop);
			// console.log("looking for id", id_tosearch);
			let foundproduct = eshop.find((product) => {
				return product.id == id_tosearch;
			});
			return foundproduct;
		},
	},
};
</script>

<style scoped>
.eshops {
	display: flex;
}

.flexx {
	display: flex;
	align-items: centered;
	position: relative;
	height: 80px;
}

h3 {
	position: relative;
	vertical-align: centered;
	/* top: 0.5em; */
}

.fullw {
	width: 100%;
}

* {
	font-family: "Roboto", sans-serif;
}
</style>
