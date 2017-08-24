declare module jspb {
export interface ExtensionFieldBinaryInfo {
	fieldInfo: jspb.ExtensionFieldInfo;
	binaryReaderFn: Function;
	binaryWriterFn: Function;
	binaryMessageSerializeFn: Function;
	binaryMessageDeserializeFn: Function;
	isPacked: boolean;
}
export interface ExtensionFieldInfo {
	fieldIndex: number;
	fieldName: string;
	ctor: any;
	ObjectFn: Function;
	isRepeated: boolean;
}
export interface Message {
}
}
declare module proto.VGFishProto{
	export const enum ErrorCode {
		E_Success = 0,
		E_Unknown = 1,
		E_WrongUrl = 2,
		E_NotSupportXHR = 3,
		E_AccountNotExist = 65537,
		E_MoneyNotEnough = 131073,
		E_TokenInvalid = 196609,
		E_Others = 262145,
	}
}
declare module proto.DDZProto {
	export class DDZMessage {
		constructor(data?: any[]);
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
		getRequest: () => Request;
		setRequest: (value: Request) => void;
		getResponse: () => Response;
		setResponse: (value: Response) => void;
		getNotify: () => Notify;
		setNotify: (value: Notify) => void;
	}
}
declare module proto.DDZProto {
	export class Request {
		constructor(data?: any[]);
		static extensions: {};
		static extensionsBinary: {};
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
		getSerial: () => number;
		setSerial: (value: number) => void;
	}
}
declare module proto.DDZProto {
	export class Response {
		constructor(data?: any[]);
		static extensions: {};
		static extensionsBinary: {};
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
		getSerial: () => number;
		setSerial: (value: number) => void;
		getErrorcode: () => ErrorCode;
		setErrorcode: (value: ErrorCode) => void;
		getErrormessage: () => string;
		setErrormessage: (value: string) => void;
		getCoin: () => number;
		setCoin: (value: number) => void;
	}
}
declare module proto.DDZProto {
	export class Notify {
		constructor(data?: any[]);
		static extensions: {};
		static extensionsBinary: {};
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
	}
}
declare module proto.DDZProto {
	export class AuthRequest {
		constructor(data?: any[]);
		static extensions: {};
		static extensionsBinary: {};
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
	}
}
declare module proto.DDZProto {
	export class AuthResponse {
		constructor(data?: any[]);
		static extensions: {};
		static extensionsBinary: {};
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
	}
}
declare module proto.DDZProto {
	export class UserLoginRequest {
		constructor(data?: any[]);
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
		getAccountname: () => string;
		setAccountname: (value: string) => void;
		getPassword: () => string;
		setPassword: (value: string) => void;
	}
}
declare module proto.DDZProto {
	export class UserLoginResponse {
		constructor(data?: any[]);
		serializeBinary: () => any;
		static deserializeBinary: (data) => any;
		getToken: () => string;
		setToken: (value: string) => void;
	}
}
declare module proto.DDZProto {
	export interface Request {
		getExtension(a: jspb.ExtensionFieldInfo);
		setExtension(a: jspb.ExtensionFieldInfo, b: jspb.Message);
	}
}
declare module proto.DDZProto {
	export var authrequest: jspb.ExtensionFieldInfo;
}
declare module proto.DDZProto {
	export interface Response {
		getExtension(a: jspb.ExtensionFieldInfo);
		setExtension(a: jspb.ExtensionFieldInfo, b: jspb.Message);
	}
}
declare module proto.DDZProto {
	export var authresponse: jspb.ExtensionFieldInfo;
}
declare module proto.DDZProto {
	export interface AuthRequest {
		getExtension(a: jspb.ExtensionFieldInfo);
		setExtension(a: jspb.ExtensionFieldInfo, b: jspb.Message);
	}
}
declare module proto.DDZProto {
	export var userlogin: jspb.ExtensionFieldInfo;
}
declare module proto.DDZProto {
	export interface AuthResponse {
		getExtension(a: jspb.ExtensionFieldInfo);
		setExtension(a: jspb.ExtensionFieldInfo, b: jspb.Message);
	}
}
declare module proto.DDZProto {
	export var userloginresponse: jspb.ExtensionFieldInfo;
}