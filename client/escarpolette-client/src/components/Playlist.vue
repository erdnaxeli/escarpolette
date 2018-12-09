<template>

	<v-data-table
			:items="items"
			class="elevation-1"
			:pagination.sync="pagination"
			:hide-actions="true"
		>
		<template slot="items" slot-scope="props">
			<td>{{ props.item.title || props.item.url }}</td>
			<td> + </td>
			<td> - </td>
		</template>
	</v-data-table>

</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			playingIndex:1,
			items: [
				{
					"_id": "5c0c57d4dc07e9251d3f9e9f",
					"playingIndex": 0,
					"title": "melody riot",
					//"isMine": true,
					//"score": 9
				},
				{
					"_id": "5c0c57d4404d9968803475c3",
					"playingIndex": 1,
					"title": "sad song",
					//"isMine": false,
					//"score": 3
				},
				{
					"_id": "5c0c57d48f06aab034adc80b",
					"playingIndex": 2,
					"title": "sad shelter",
					//"isMine": false,
					//"score": 0
				},
				{
					"_id": "5c0c57d45c042cb0ce884608",
					"playingIndex": 3,
					"title": "blood shelter",
					//"isMine": true,
					//"score": 1
				},
				{
					"_id": "5c0c57d4c3aa27fbb3f6a709",
					"playingIndex": 4,
					"title": "blood song",
					//"isMine": false,
					//"score": 6
				},
				{
					"_id": "5c0c57d4f78bc49aca6978d8",
					"playingIndex": 5,
					"title": "melody song",
					//"isMine": true,
					//"score": 5
				}
			],
			pagination: {
				//sync: {
					rowsPerPage: -1,
				//}
			}
		}
	},
	created: function() {
		axios.get(`http://192.168.1.28:5000/items`)
    .then(response => {
      // JSON responses are automatically parsed.
      //this.items = response.data
      console.log(response)
    })
	}

}

/*
[
	{
		'repeat(5, 10)': {
			_id: '{{objectId()}}',
			title: '{{random("blood", "melody", "sad")}} {{random("song", "riot", "shelter")}}',
			artist: '{{firstName()}} {{surname()}}',
			isMine: '{{bool()}}',
			url: 'youtu.be/yoursong',
			img: 'http://placehold.it/50x50',
		}
	}
]
*/
</script>

