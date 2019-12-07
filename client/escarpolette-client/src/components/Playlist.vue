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
							<template  v-if="props.item.playingIndex == playingIndex">
								<v-icon size="30" color="white">play_arrow</v-icon>
								<span class="white--text"> {{timer | displayTimer}} </span>
							</template>
							<v-icon v-else-if="props.item.playingIndex < playingIndex" size="25" disabled style="opacity: 0.3">add_circle_outline</v-icon>
							<v-icon v-else size="30" color="primary">{{ props.item.iVoted ? 'add_circle_outline' : 'remove_circle'}}</v-icon>
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
			playingIndex: 1,
			timePlayed: 150,
			items: [
				{
					"_id": "5c0c57d4dc07e9251d3f9e9f",
					"playingIndex": 0,
					"url": "melody riot",
					"iVoted": true,
					"duration": 180
					//"isMine": true,
					//"score": 9
				},
				{
					"_id": "5c0c57d4404d9968803475c3",
					"playingIndex": 1,
					"url": "sad song",
					"iVoted": false,
					"duration": 180
					//"isMine": false,
					//"score": 3
				},
				{
					"_id": "5c0c57d48f06aab034adc80b",
					"playingIndex": 2,
					"url": "sad shelter",
					"iVoted": false,
					"duration": 180
					//"isMine": false,
					//"score": 0
				},
				{
					"_id": "5c0c57d45c042cb0ce884608",
					"playingIndex": 3,
					"url": "blood shelter",
					"iVoted": true,
					"duration": 180
					//"isMine": true,
					//"score": 1
				},
				{
					"_id": "5c0c57d4c3aa27fbb3f6a709",
					"playingIndex": 4,
					"url": "blood song",
					"iVoted": false,
					"duration": 180
					//"isMine": false,
					//"score": 6
				},
				{
					"_id": "5c0c57d4f78bc49aca6978d8",
					"playingIndex": 5,
					"url": "melody song",
					"iVoted": true,
					"duration": 180
					//"isMine": true,
					//"score": 5
				}
			],
			pagination: {
				rowsPerPage: -1,
			},
			timer: 0,
			interval: null
		}
	},
	filters: {
		displayTimer: function(value) {
			console.log(value)
			const minutes = Math.floor(value / 60);
			const sec = value % 60;
			return minutes + ":" + sec
		}
	},
	created: function() {
		const vm = this;
		axios.get(`http://192.168.1.28:5000/items`)
		.then(response => {
			// JSON responses are automatically parsed.
			this.updatePlaylist()
		})
	},
	methods: {
		updatePlaylist: function() {
			const vm = this;
			axios.get(`http://192.168.1.28:5000/items`)
			.then(response => {
				// JSON responses are automatically parsed.
				 console.log(response.data.playlist)
				 this.timer = this.timePlayed;
				 this.interval = setInterval(this.incrementTimer, 1000)
			})
		},
		incrementTimer: function() {
			// later: do it according date timestamp
			this.timer++;
			if(this.timer >= this.items[this.playingIndex].duration) {
				clearInterval(this.interval)
				this.updatePlaylist()
			}
		}
	},

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

