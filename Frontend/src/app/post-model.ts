export class Post {
	url: string;
	title: string;
	image: string;
	pub_date: string;
	comments: Comment[];
}

class Comment {
	pk: number;
	text: string;
	pub_date: string;
	user: number;
	post: number;
	replies: Reply[];
}

class Reply {
	text: string;
	pub_date: string;
	user: number;
}