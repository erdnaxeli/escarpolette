<template>

	<v-data-table
			:items="items"
			:pagination.sync="pagination" :hide-headers= "true" :hide-actions="true"
			class="elevation-1"
		>
		<template slot="items" slot-scope="props">
				<tr :class="props.item.playingIndex == playingIndex ? 'accent white--text' : props.item.playingIndex < playingIndex ? 'secondary' : ''">
					<td>{{ props.item.url }}</td>
					<td style="max-width:100px">
						<v-btn flat icon>
							<v-icon v-if="props.item.playingIndex == playingIndex" size="40" color="white">play_arrow</v-icon>
							<v-icon v-else-if="props.item.playingIndex < playingIndex" size="25" disabled>star</v-icon>
							<v-icon v-else size="30" color="primary">{{ props.item.iVoted ? 'star' : 'star_border'}}</v-icon>
						</v-btn>
					</td>
				</tr>
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
					"url": "melody riot",
					"iVoted": true,
					//"isMine": true,
					//"score": 9
				},
				{
					"_id": "5c0c57d4404d9968803475c3",
					"playingIndex": 1,
					"url": "sad song",
					"iVoted": false,
					//"isMine": false,
					//"score": 3
				},
				{
					"_id": "5c0c57d48f06aab034adc80b",
					"playingIndex": 2,
					"url": "sad shelter",
					"iVoted": false,
					//"isMine": false,
					//"score": 0
				},
				{
					"_id": "5c0c57d45c042cb0ce884608",
					"playingIndex": 3,
					"url": "blood shelter",
					"iVoted": true,
					//"isMine": true,
					//"score": 1
				},
				{
					"_id": "5c0c57d4c3aa27fbb3f6a709",
					"playingIndex": 4,
					"url": "blood song",
					"iVoted": false,
					//"isMine": false,
					//"score": 6
				},
				{
					"_id": "5c0c57d4f78bc49aca6978d8",
					"playingIndex": 5,
					"url": "melody song",
					"iVoted": true,
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
			// this.items = response.data.playlist
			 console.log(this.items)
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

